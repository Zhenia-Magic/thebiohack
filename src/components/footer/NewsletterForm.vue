<template>
  <q-form
    @submit="onSubmit"
    class="column form">
    <section-header>
      Subscribe to Newsletter
    </section-header>
    <q-input
      bg-color="white"
      color="dark"
      label="Email"
      rounded
      outlined
      v-model="email"
      type="email"
      class="margin-auto">
    </q-input>
    <div class="row names no-wrap">
      <q-input
        bg-color="white"
        color="dark"
        label="First Name"
        rounded
        outlined
        v-model="firstName">
      </q-input>
      <q-input
        bg-color="white"
        color="dark"
        label="Last Name"
        rounded
        outlined
        v-model="lastName"
        class="name-second">
      </q-input>
    </div>
    <q-btn
      rounded
      class="submit-button"
      label="Subscribe"
      type="submit"
      color="accent"/>
  </q-form>
</template>

<script>
import { ref } from 'vue';
import SectionHeader from 'components/UI/SectionHeader.vue';

export default {
  name: 'NewsletterForm',
  components: { SectionHeader },
  setup() {
    const email = ref('');
    const firstName = ref('');
    const lastName = ref('');
    const onSubmit = () => '';
    return {
      email,
      firstName,
      lastName,
      onSubmit,
    };
  },
};

</script>

<style scoped>

.names {
  margin-top: 1.7em;
}

.name-second {
  margin-left: 0.7rem
}

.submit-button {
  margin: 1.7rem auto 0 auto;
}

.form {
  padding: 2rem 0.5rem 2rem 0.5rem;
  flex-basis: 23rem;
}

</style>
