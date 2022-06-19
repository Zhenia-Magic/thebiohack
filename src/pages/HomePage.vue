<template>
  <q-page class="bg-secondary">
    <div class="content row q-pa-none" style="padding-top: 1%">
      <div class="col-8 bg-secondary">
        <div class="q-pa-md" style="border-radius: 1em">
          <h4 class="text-accent" style="font-size: 1.5em;
          font-weight: bold; text-align: center">
            {{ $route.params.articleID }}
          </h4>

        </div>
      </div>
      <div class="col-4 bg-secondary">
        <div class=" q-ma-md q-pa-md" style="border-radius: 1em">
          <h5 class="text-accent" style="font-size: 1.5em;
          font-weight: bold; text-align: center">
            Contents
          </h5>
          <q-list class>
            <q-item clickable v-ripple class="content-item">
              <q-item-section>Sleep</q-item-section>
            </q-item>

            <q-item clickable v-ripple class="content-item">
              <q-item-section>
                <q-item-label>Nutrition</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="content-item">
              <q-item-section>
                <q-item-label>Work</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="content-item">
              <q-item-section>
                <q-item-label>Exercise</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="content-item">
              <q-item-section>
                <q-item-label>Brain</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'HomePage.vue',
};
</script>

<style scoped>

.content-item {
  background-color: #904c77ff;
  padding: 1em;
  margin: 1em 0em;
  border-radius: 1em;
  text-align: center;
  color: white;
  font-weight: bold;
  font-size: 1.5em;
  max-width: 10em;
}

.article {
  margin: 0em 3em;
  font-size: 1rem;
  text-align: justify;
}
</style>
