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
import { ref } from "vue";

export default {
  name: 'HomePage.vue',
  components: { ArticlesList, TopicsList },
  setup() {
    const selectedSort = ref('');
    const sortOptions = ref([
      { value: '', name: 'All' },
      { value: 'sleep', name: 'Sleep' },
      { value: 'nutrition', name: 'Nutrition' },
      { value: 'work', name: 'Work' },
      { value: 'exercise', name: 'Exercise' },
      { value: 'brain', name: 'Brain' },
    ]);
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
