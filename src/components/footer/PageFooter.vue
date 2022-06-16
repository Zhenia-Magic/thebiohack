<template>
  <footer>
    <div class="footer shadow-up-2">
      <div class="row justify-center items-stretch reverse-wrap">
        <site-menu
          class="col-xs-4 col-sm-4 col-md-4 col-lg-3 col-xl-2"/>
        <newsletter-form
          class="col-xs-10 col-sm-6 col-md-6 col-lg-3 col-xl-auto"/>
      </div>
      <social-icons/>
    </div>
  </footer>
</template>

<script>
import NewsletterForm from './NewsletterForm.vue';
import SiteMenu from './SiteMenu.vue';
import SocialIcons from './SocialIcons.vue';

export default {
  name: 'PageFooter',
  components: { SiteMenu, NewsletterForm, SocialIcons },
};
</script>

<style scoped>
footer {
  padding-top: 1%;
  background: var(--q-secondary);
}

.footer {
  background: var(--q-primary);
  min-height: 200px;
}

</style>
