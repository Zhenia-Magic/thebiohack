<template>
  <q-page class="bg-secondary">
    <div class="flex row justify-center q-pt-md"
         v-if="$q.screen.gt.sm">
      <div class="col-7 bg-secondary">
        <articles-list
          :selectedSort="selectedSort"
        />
      </div>
      <div class="col-3 bg-secondary">
      <topics-list
        @updateSelectedSort="updateSelectedSort"
        :options="sortOptions"
        orientation="vertical"
      />
      </div>
    </div>

    <div class="flex column q-pa-none" v-else>
      <topics-list
        @updateSelectedSort="updateSelectedSort"
        :options="sortOptions"
        orientation="horizontal"
      />
      <articles-list
        :selectedSort="selectedSort"
      />
    </div>
  </q-page>
</template>

<script>
import TopicsList from 'components/articles/TopicsList.vue';
import ArticlesList from 'components/articles/ArticlesList.vue';
import { ref } from 'vue';
import { api } from 'boot/axios';
import { useQuasar } from 'quasar';

export default {
  name: 'HomePage.vue',
  components: { ArticlesList, TopicsList },
  setup() {
    const sortOptions = ref(null);
    const $q = useQuasar();

    function loadTags() {
      api.get('/tags')
        .then((response) => {
          const { data } = response;
          data.forEach((element) => {
            element.value = element.name.toLowerCase();
          });
          data.unshift({ id: 0, name: 'All', value: '' });
          sortOptions.value = data;
        })
        .catch(() => {
          $q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem',
          });
        });
    }
    loadTags();
    const selectedSort = ref('');
    const updateSelectedSort = (option) => {
      selectedSort.value = option;
    };
    return {
      selectedSort,
      sortOptions,
      updateSelectedSort,
    };
  },
};
</script>

<style scoped>

</style>
