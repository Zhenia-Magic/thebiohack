<template>
  <q-page class="window-height">
    <div class="row q-pa-none" style="height: 100vh; padding-top: 53px;
    padding-bottom: 0">
      <div class="col-8 bg-secondary">
        <div class="bg-primary q-ma-md q-pa-md" style="border-radius: 1em">
          <h4 class="text-accent" style="font-size: 1.5em;
          font-weight: bold; text-align: center">
            ARTICLE'S TITLE
          </h4>
          <div class="article">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            <br><br>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            <br><br>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.Lorem ipsum dolor
            sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
            <br><br>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab accusamus
            aperiam aspernatur debitis dicta dolor eius eveniet fuga hic in minima
            molestias omnis provident quam quod, repellat, sunt vero.
          </div>
        </div>
      </div>
      <div class="col-4 bg-secondary">
        <div class="bg-primary q-ma-md q-pa-md" style="border-radius: 1em">
          <h5 class="text-accent" style="font-size: 1.5em;
          font-weight: bold; text-align: center">
            CONTENTS
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

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
});
</script>

<style lang="scss">
.content-item {
  background-color: #904c77ff;
  padding: 1em;
  margin: 1em 0em;
  border-radius: 1em;
  text-align: center;
  color: white;
  font-weight: bold;
  font-size: 1.5em;
}

.article {
  margin: 0em 3em;
  font-size: 1.3rem;
  text-align: justify;
}

</style>
