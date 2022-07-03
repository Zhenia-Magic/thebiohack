import { defineStore } from 'pinia';

export const useMainStore = defineStore('main', {
  state: () => ({
    websiteSection: '/',
  }),
  getters: {},
  actions: {
    setWebsiteSection(link: string) {
      this.websiteSection = link;
    },
  },
});
