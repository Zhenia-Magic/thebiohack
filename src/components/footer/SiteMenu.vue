<template>
  <div class="menu"
       :class="{ 'flex': $q.screen.lt.sm}">
    <section-header>
      Resources
    </section-header>
    <div class="flex column menu-items">
      <p class="menu-item"><router-link to="/course">Home</router-link></p>
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

.menu {
  padding: 2rem 0 2rem 0;
}

.menu-item {
  margin: 0;
  padding: 0;
  color: var(--q-dark);
  max-width: 72%;
}

a, a:visited {
  text-decoration: none;
  color: inherit;
}

.menu-item:hover {
  font-weight: 600;
}

.menu-items {
  height: 80%;
  justify-content: space-between;
  font-size: 1.15em;
  font-weight: 500;
  min-height: 199px;
}

@media (max-width: 599px) {
  .menu-items {
    width: 100%;
    align-items: center;
  }
}
</style>
