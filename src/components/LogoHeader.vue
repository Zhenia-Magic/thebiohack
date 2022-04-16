<template>
  <q-header class="bg-accent">
    <q-img class="row justify-center q-pa-none xs-hide"
      src="src/assets/logo.png"
      spinner-color="white"
      loading="eager"
      style="max-width: 80%; margin: auto"
    />
    <q-img class="row justify-center q-pa-none q-ma-none sm-hide md-hide lg-hide xl-hide"
      src="src/assets/logo_letters.png"
      spinner-color="white"
      loading="eager"
      style="max-width: 40%; margin: auto"/>
  </q-header>
</template>

<script>
export default {
  name: 'LogoHeader',
};
</script>

<style scoped>

</style>
