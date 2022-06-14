<template>
      <div class="navbar">
        <q-toolbar class="bg-primary text-accent bottom-shadow">
          <q-btn-dropdown dropdown-icon="menu" flat round dense
          class="sm-hide md-hide lg-hide xl-hide">
            <q-list bordered separator class="bg-accent text-white">
              <q-item clickable v-close-popup v-for="option in options" :key="option.value">
                <q-item-section>
                  <q-item-label>{{ option.label }}</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
          <q-space />
          <q-btn-toggle
            v-model="model"
            no-caps
            flat no-wrap stretch class="ellipsis xs-hide text-bold"
            toggle-color="dark"
            :options="options"
            padding="0.7em 2em"
            size="1.5em"
          />
          <q-space />
        </q-toolbar>
      </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    return {
      model: ref('tutorials'),
      options: ref([
        { label: 'Tutorials', value: 'tutorials' },
        { label: 'Challenges', value: 'challenges' },
        { label: 'Tech Devices', value: 'tech_devices' },
        { label: 'Community', value: 'community' },
      ]),
    };
  },
};
</script>

<style>
.q-btn {
  font-weight: 900;
}

.navbar {
  position: sticky;
  top: 0;
}

.bottom-shadow {
  box-shadow: 0 4px 2px -3px gray;
}

</style>
