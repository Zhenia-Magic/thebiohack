<template>
  <div
    class="flex column no-wrap q-ma-md q-pa-md articles justify-between"
  >
    <article-card
      v-for="post in postsOnPage"
      :title="post.title"
      :text="post.text"
      :topic="post.topic"
      :key="post.name"
    />
    <div class="q-pb-none q-pt-md flex flex-center">
      <q-pagination
        v-model="page"
        :max="maxPages"
        color="accent"
        boundary-links
      >
      </q-pagination>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import ArticleCard from 'components/articles/ArticleCard.vue';

export default {
  name: 'articles-list',
  components: { ArticleCard },
  props: {
    selectedSort: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const textVal = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci atque cum dolor dolore, doloribus ducimus eaque error illum laborum maxime modi neque nobis officia provident, quia quis saepe temporibus. Sit?';
    const posts = ref([
      {
        title: 'Post 1', text: textVal, topic: 'sleep', attrs: { to: '/' },
      },
      {
        title: 'Post 2', text: textVal, topic: 'nutrition', attrs: { to: '/course' },
      },
      {
        title: 'Post 3', text: textVal, topic: 'exercise', attrs: { to: '/challenges' },
      },
      {
        title: 'Post 4', text: textVal, topic: 'brain', attrs: { to: '/community' },
      },
      {
        title: 'Post 5', text: textVal, topic: 'work', attrs: { to: '/community' },
      },
      {
        title: 'Post 6', text: textVal, topic: 'work', attrs: { to: '/' },
      },
      {
        title: 'Post 7', text: textVal, topic: 'nutrition', attrs: { to: '/course' },
      },
      {
        title: 'Post 8', text: textVal, topic: 'exercise', attrs: { to: '/challenges' },
      },
      {
        title: 'Post 9', text: textVal, topic: 'brain', attrs: { to: '/community' },
      },
      {
        title: 'Post 10', text: textVal, topic: 'work', attrs: { to: '/community' },
      },
    ]);
    const limit = ref(4);
    const page = ref(1);
    const currentPage = ref(1);
    const nextPage = ref(null);
    const sortedPosts = computed(
      () => posts.value.filter((post) => post.topic.includes(props.selectedSort)),
    );
    const postsOnPage = computed(() => (sortedPosts.value.slice(
      (page.value - 1) * limit.value,
      (page.value - 1) * limit.value + limit.value,
    )));
    const maxPages = computed(() => Math.ceil(sortedPosts.value.length / limit.value));
    return {
      posts,
      postsOnPage,
      limit,
      page,
      currentPage,
      nextPage,
      maxPages,
    };
  },
};
</script>

<style scoped>

.articles {
  border-radius: 1em
}

@media (min-width: 600px) {
  .articles { margin-left: 32px; }
}

</style>
