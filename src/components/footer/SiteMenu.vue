<template>
  <div class="menu">
    <h6>Resources</h6>
    <div class="flex column menu-items">
      <p>Home</p>
      <p>About</p>
      <p>Contact Us</p>
      <p>Terms of Use</p>
      <p>Privacy Policy</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'SiteMenu',
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

p {
  margin: 0;
  color: var(--q-dark);
  max-width: 30%;
}

p:hover {
  font-weight: 600;
}

.menu-items {
  height: 80%;
  justify-content: space-between;
  font-size: 1.15em;
  font-weight: 500;
}
</style>
