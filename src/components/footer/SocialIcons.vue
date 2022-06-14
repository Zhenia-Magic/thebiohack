<template>
  <div class="column justify-center items-center">
    <h6>Follow Us</h6>
    <div class="row social-icons q-pb-md">
      <q-icon
        size="2em"
        class="icon bi bi-telegram" />
      <q-icon
        size="2em"
        class="icon bi bi-facebook" />
      <q-icon
        size="2em"
        class="icon bi bi-instagram" />
      <q-icon
        size="2em"
        class="icon bi bi-pinterest" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SocialIcons',
};
</script>

<style scoped>
.icon {
  padding: 0 0.7em 0 0.7em;
  color: var(--q-dark)
}

.social-icons {
  margin: auto;
}

h6 {
  color: var(--q-dark);
  font-weight: 900;
  margin: 0 auto 1em auto;
}

</style>
