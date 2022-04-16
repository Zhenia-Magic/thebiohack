<template>
  <q-layout view="hhh lpr fff" >
    <LogoHeader/>
    <PageFooter />
    <NavBarDropdown/>
    <q-page-container>
      <router-view />
    </q-page-container>
    <NavBar/>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import NavBar from 'components/NavBar.vue';
import LogoHeader from 'components/LogoHeader.vue';
import PageFooter from 'components/PageFooter.vue';

export default defineComponent({
  name: 'MainLayout',
  components: { NavBar, LogoHeader, PageFooter },
});
</script>
