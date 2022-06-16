<template>
  <q-layout view="hhh lpr fff" >
    <logo-header/>
    <nav-bar class="sticky"/>
    <div class="body">
      <q-page-container>
        <router-view />
      </q-page-container>
      <page-footer />
    </div>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import NavBar from 'components/navbar/NavBar.vue';
import LogoHeader from 'components/navbar/LogoHeader.vue';
import PageFooter from 'components/footer/PageFooter.vue';

export default defineComponent({
  name: 'MainLayout',
  components: {
    NavBar,
    LogoHeader,
    PageFooter,
  },
});
</script>

<style scoped>
.body {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

q-page-container {
  flex: 1
}
.sticky {
  z-index: 1
}

</style>
