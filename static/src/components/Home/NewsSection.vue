<template>
  <div class="row q-px-md q-col-gutter-lg-md">
      <div class="col-xs-12 col-md-6">
          <div class="category_title_container">
              <p class="text-h5 ">Category One</p>
          </div>
          <div class="row q-col-gutter-sm">
              <div id="big_side" class="col-xs-12 col-sm-6">
                  <news-card :title="'Title Big'"
                  :body="'Body big'"
                  :subtitle="'by John Doe'" />
              </div>
              <div id="small_side" class="col-xs-12 col-sm-6 ">
                  <div class="q-mb-sm"  v-for="n in 4" :key="n">

                  <news-card :title="'Title Small add some to it test mike one two tesitng ellipsis'"
                  :body="'Body small'"
                  :subtitle="'by John Doe'" horizontal />
                  </div>
              </div>
          </div>
      </div>
      <div class="col-xs-12 col-md-6  " :class="{
          'q-mt-lg' : $q.screen.lt.md, 'q-mt-none': $q.screen.gt.sm 
      }">
          <div class="category_title_container">
              <p class="text-h5">Category Two</p>
          </div>
          <div class="row q-col-gutter-sm">
              <div id="big_side" class="col-xs-12 col-sm-6">
                  <news-card :title="'Title Big'"
                  :body="'Body big'"
                  :subtitle="'by John Doe'" />
              </div>
              <div id="small_side" class="col-xs-12 col-sm-6 ">
                  <div class="q-mb-sm"  v-for="n in 4" :key="n">

                  <news-card :title="'Title Small'"
                  :body="'Body small'"
                  :subtitle="'by John Doe'" horizontal />
                  </div>
              </div>
          </div>
      </div>
  </div>
  <div class=" q-mt-md-xl flex justify-center">
      <q-btn label="Read More" color="secondary" type="a" href="#" />
  </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue"
</script>

<style lang="sass">
.category_title_container
    width: 98%
    color: #fff
    margin-bottom: 20px
    border-bottom: 2px $primary solid
    p.text-h5
        padding-left: 10px
        padding-right: 10px
        padding-top: 2px
        padding-bottom: 2px
        width: fit-content
        background-color: $primary
        margin-bottom: 0
            // line-height: 0
</style>