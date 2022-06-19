import { RouteRecordRaw } from 'vue-router';
import MainLayout from 'src/layouts/MainLayout.vue';
import ArticlePage from 'src/pages/ArticlePage.vue';
import ChallengesPage from 'src/pages/ChallengesPage.vue';
import CommunityPage from 'src/pages/CommunityPage.vue';
import TechDevicesPage from 'src/pages/TechDevicesPage.vue';
import HomePage from 'src/pages/HomePage.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '',
        component: HomePage,
        children: [{
          path: 'articles/:articleID',
          component: ArticlePage,
        }],
      },
      {
        path: 'challenges',
        component: ChallengesPage,
      },
      {
        path: 'community',
        component: CommunityPage,
      },
      {
        path: 'tech-devices',
        component: TechDevicesPage,
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
