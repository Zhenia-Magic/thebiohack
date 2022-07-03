<template>
  <div
    v-if="orientation === 'horizontal'"
    class="flex column q-mt-xl q-mx-md q-px-md q-pb-none"
    style="border-radius: 1em">
    <section-header class >Topics</section-header>
    <q-list class="flex row col-gap">
      <q-item
          clickable
          v-ripple
          class="content-item"
          v-for="option in options"
          :key="option.value"
          @click="$emit('updateSelectedSort', option.value)">
        <q-item-section>{{ option.name }}</q-item-section>
      </q-item>
    </q-list>
  </div>

  <div
    v-else
    class="flex column q-ma-md q-pa-md"
    style="border-radius: 1em">
    <section-header class >Topics</section-header>
    <q-list class="flex column">
      <q-item
        clickable
        v-ripple
        class="content-item"
        v-for="option in options"
        :key="option.value"
        @click="$emit('updateSelectedSort', option.value)">
        <q-item-section>{{ option.name }}</q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import SectionHeader from 'components/UI/SectionHeader.vue';

export default {
  name: 'topics-list',
  components: { SectionHeader },
  props: {
    options: {
      type: Array,
      required: true,
    },
    orientation: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.content-item {
  background-color: #904c77ff;
  padding: 1em;
  margin: 0.7em auto 0.7em auto;
  border-radius: 1em;
  text-align: center;
  color: white;
  font-weight: bold;
  font-size: 1.5em;
  min-width: 11.3em;
}

.col-gap {
  column-gap: 10px;
}

</style>
