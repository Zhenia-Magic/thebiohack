<template>
  <h6 class="header">
    <slot></slot>
  </h6>
</template>

<script>
export default {
  name: 'SectionHeader',
};
</script>

<style scoped>
.header {
  color: var(--q-dark);
  font-weight: 900;
  margin: 0 auto 1em auto;
}
</style>
