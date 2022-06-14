<template>
  <div class="menu">
    <h6>Resources</h6>
    <div>
      <p>Home</p>
      <p>About</p>
      <p>Contact Us</p>
      <p>Terms of Use</p>
      <p>Privacy Policy</p>
    </div>
  </div>
</template>

<script>
import SocialIcons from './SocialIcons.vue';

export default {
  name: 'MenuWithIcons',
};
</script>

<style scoped>
h6 {
  color: var(--q-dark);
  font-weight: 900;
  margin: 0 auto 1em auto;
}

.menu {
  padding: 2rem 0 2rem 0;
}

</style>
