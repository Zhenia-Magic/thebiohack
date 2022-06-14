<template>
  <q-form
    @submit="onSubmit"
    class="column form justify-stretch content-stretch">
    <h6>Subscribe to Newsletter</h6>
    <q-input
      bg-color="white"
      color="dark"
      label="Email"
      rounded
      outlined
      v-model="email"
      type="email">
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

export default {
  name: 'NewsletterForm',
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
  margin: 1.7em auto auto auto
}

.name-second {
  margin-left: 0.7rem
}

.submit-button {
  margin: 1.7rem auto 0 auto;
}

.form {
  padding: 2rem 0 2rem 0;
}

h6 {
  color: var(--q-dark);
  font-weight: 900;
  margin: 0 auto 1em auto;
}

</style>
