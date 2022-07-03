<template>
  <q-card
    v-ripple
    bordered
    flat
    class="xs-hide my-card cursor-pointer q-hoverable"
    @click="this.$router.push(`/articles/${toSpinalCase(title)}`)"
  >
    <q-card-section horizontal class="height">
      <q-img
        fit="cover"
        src="https://cdn.quasar.dev/img/mountains.jpg"
      />
      <q-card-section class="col-7 q-pt-sm container">
        <div class="text-h6">{{ title }}</div>
        <div class="text-subtitle2 overflow-text">{{ text }}</div>
        <div class="tags flex">
          <q-badge class="q-mt-md tag" :class="topic" outline :label="topic" />
        </div>
      </q-card-section>
    </q-card-section>
  </q-card>
  <q-card v-ripple bordered
          flat class="my-card sm-hide md-hide lg-hide xl-hide cursor-pointer q-hoverable"
          @click="this.$router.push(`/articles/${toSpinalCase(title)}`)">
    <q-img
      fit="cover"
      src="https://cdn.quasar.dev/img/mountains.jpg"
    />

    <q-card-section class="flex column">
      <div class="text-h6">{{ title }}</div>
      <div class="text-subtitle2 overflow-text">{{ text }}</div>
      <div class="flex">
        <q-badge class="q-mt-md tag" :class="topic" outline :label="topic" />
      </div>
    </q-card-section>
  </q-card>
</template>

<script>

export default {
  name: 'article-card',
  props: {
    title: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
    topic: {
      type: String,
      required: true,
    },
  },
  setup() {
    const toSpinalCase = (str) => str.replace(/( |_)+/g, '-').replace(/([a-z])(?=[A-Z])/g, '$1-').toLowerCase();
    return {
      toSpinalCase,
    };
  },
};
</script>

<style scoped>
.my-card {
  min-height: 0;
  margin-bottom: 1.5em;
}
.height {
  height: 200px;
}

.my-card:hover {
  outline: solid 2px var(--q-accent);
}

.overflow-text {
  text-align: justify;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -moz-box-orient: vertical;
  -ms-box-orient: vertical;
  box-orient: vertical;
  -webkit-line-clamp: 5;
  -moz-line-clamp: 5;
  -ms-line-clamp: 5;
  line-clamp: 5;
}

.tags {
  position: absolute;
  bottom: 15px;
}

.tag {
  transform: scale(1.3);
  margin-left: 4px;
  margin-right: 20px;
}

.sleep {
  color: rebeccapurple;
}

.exercise {
  color: dodgerblue;
}

.nutrition {
  color: orange;
}

.work {
  color: green;
}

.brain {
  color: deeppink;
}

.container {
  position: relative
}

</style>
