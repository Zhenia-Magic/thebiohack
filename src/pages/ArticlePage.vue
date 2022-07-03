<template>
  <q-page class="bg-secondary">
    <div class="content row q-pa-none" style="padding-top: 1%">
      <div class="col-8 bg-secondary">
        <div class="q-pa-md" style="border-radius: 1em">
          <h4 class="text-accent" style="font-size: 1.5em;
          font-weight: bold; text-align: center">
            {{ $route.params.articleID }}
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
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ArticlePage',
});
</script>

<style lang="scss" scoped>

.content {

}

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
  font-size: 1rem;
  text-align: justify;
}

</style>
