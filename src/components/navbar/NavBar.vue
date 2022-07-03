<template>
      <div class="navbar">
        <q-toolbar class="bg-primary text-accent bottom-shadow">
          <q-btn-dropdown dropdown-icon="menu" flat round dense
          class="sm-hide md-hide lg-hide xl-hide">
            <q-list bordered separator class="bg-accent text-white">
              <q-item
                class="item"
                clickable
                v-close-popup
                v-for="option in options"
                :key="option.value"
                :active="store.websiteSection === option.value"
                @click="redirectPage(option)"
                active-class="active-item">
                <q-item-section>
                  <q-item-label>
                      {{ option.label }}
                  </q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
          <q-space />
          <q-btn-toggle
            v-model="store.websiteSection"
            no-caps
            flat no-wrap stretch class="ellipsis xs-hide text-bold"
            toggle-color="dark"
            :options="options"
            padding="0.7em 2em"
            size="22px"
          />
          <q-space />
        </q-toolbar>
      </div>
</template>

<script>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useMainStore } from 'stores/main-store';

export default {
  setup() {
    const router = useRouter();
    const store = useMainStore();
    store.setWebsiteSection(router.currentRoute.value.path.slice(1));

    watch(() => router.currentRoute.value.path, () => {
      store.setWebsiteSection(router.currentRoute.value.path.slice(1));
    }, { deep: true, immediate: true });
    return {
      store,
      redirectPage: (option) => {
        store.setWebsiteSection(option.value);
        router.push(option.attrs.to);
      },
      options: ref([
        { label: 'Articles', value: 'articles', attrs: { to: '/articles' } },
        { label: 'Course', value: 'course', attrs: { to: '/course' } },
        { label: 'Challenges', value: 'challenges', attrs: { to: '/challenges' } },
        { label: 'Community', value: 'community', attrs: { to: '/community' } },
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

.active-item {
  color: var(--q-dark);
  background: var(--q-primary)
}

.item {
  font-weight: 900;
}
</style>
