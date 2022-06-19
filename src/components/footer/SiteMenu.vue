<template>
  <div class="menu">
    <section-header>
      Resources
    </section-header>
    <div class="flex column menu-items">
      <p class="menu-item">Home</p>
      <p class="menu-item">About</p>
      <p class="menu-item">Contact Us</p>
      <p class="menu-item">Terms of Use</p>
      <p class="menu-item">Privacy Policy</p>
    </div>
  </div>
</template>

<script>
import SectionHeader from 'components/UI/SectionHeader.vue';

export default {
  name: 'SiteMenu',
  components: { SectionHeader },
};
</script>

<style scoped>

.menu-header {
  color: var(--q-dark);
  font-weight: 900;
  margin: 0 auto 1em auto;
}

.menu {
  padding: 2rem 0 2rem 0;
}

.menu-item {
  margin: 0;
  color: var(--q-dark);
  max-width: 72%;
}

.menu-item:hover {
  font-weight: 600;
}

.menu-items {
  height: 80%;
  justify-content: space-between;
  font-size: 1.15em;
  font-weight: 500;
}
</style>
