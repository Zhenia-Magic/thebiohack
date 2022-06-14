<template>
  <div class="head q-pa-none">
    <q-img class="row justify-center q-pa-none xs-hide big-logo"
      src="~/src/assets/logo.png"
      spinner-color="white"
      loading="eager"
    />
    <q-img class="row justify-center q-pa-none q-ma-none sm-hide md-hide lg-hide xl-hide small-logo"
      src="~/src/assets/logo_letters.png"
      spinner-color="white"
      loading="eager"
    />
  </div>
</template>

<script>
export default {
  name: 'LogoHeader',
};
</script>
<style scoped>
.head {
  background: linear-gradient(180deg, var(--q-accent) 20%, var(--q-primary) 95%);
  padding-bottom: 10px;
}
.big-logo {
  max-width: 80%;
  margin: auto
}
.small-logo {
  max-width: 40%;
  margin: auto
}
</style>
