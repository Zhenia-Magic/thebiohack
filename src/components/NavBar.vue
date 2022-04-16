<template>
      <q-page-sticky expand position="top">
        <q-toolbar class="bg-primary text-accent shadow-2">
          <q-btn-dropdown no-icon-animation="true" dropdown-icon="menu" flat round dense
          class="sm-hide md-hide lg-hide xl-hide">
            <q-list bordered separator class="bg-accent text-white">
              <q-item clickable v-close-popup>
                <q-item-section>
                  <q-item-label>Tutorials</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup>
                <q-item-section>
                  <q-item-label>Challenges</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup>
                <q-item-section>
                  <q-item-label>Tech Devices</q-item-label>
                </q-item-section>
              </q-item>

              <q-item clickable v-close-popup>
                <q-item-section>
                  <q-item-label>Community</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
          <q-space />
          <q-btn-toggle
            v-model="model"
            flat no-wrap stretch class="ellipsis xs-hide"
            toggle-color="dark"
            :options="options"
            padding="0.7em 2em"
            size="1.3em"
          />
          <q-space />
        </q-toolbar>
      </q-page-sticky>
</template>

<script>
import { ref } from 'vue';

export default {

  setup() {
    return {
      model: ref('tutorials'),
      options: [
        { label: 'Tutorials', value: 'tutorials' },
        { label: 'Challenges', value: 'challenges' },
        { label: 'Tech Devices', value: 'tech_devices' },
        { label: 'Community', value: 'community' },
      ],
    };
  },
};
</script>
