import { RouteRecordRaw } from 'vue-router';
import MainLayout from 'src/layouts/MainLayout.vue';
import ArticlePage from 'src/pages/ArticlePage.vue';
import ChallengesPage from 'src/pages/ChallengesPage.vue';
import CommunityPage from 'src/pages/CommunityPage.vue';
import CoursePage from 'src/pages/CoursePage.vue';
import HomePage from 'src/pages/HomePage.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: 'articles',
        component: HomePage,
      },
      {
        path: 'articles/:articleID',
        component: ArticlePage,
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
        path: 'course',
        component: CoursePage,
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
