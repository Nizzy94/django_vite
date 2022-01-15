<template>
  <div class="bg-dark text-white">
      <div class="q-pa-md bg-grey-10 ">
           <div class="flex items-center justify-center">
            <div class="text-h6">
                Footer Header
            </div>
          </div>
      </div>
      <!-- <q-separator dark /> -->
      <div class="q-pa-md">
          <div style="height: 400px" class="flex items-center justify-center">
          <div class="text-h3">
              Footer Body
          </div>
              
          </div>
      </div>
      <!-- <q-separator dark /> -->
      <div class="q-pa-md  bg-grey-10 ">
          <div :class="{
              'column reverse items-center': $q.screen.lt.md,
              'flex justify-between items-center': $q.screen.gt.sm,
              }">
              <div
               :class="{
                  'q-mt-md': $q.screen.lt.md
              }">
                  
                  <div class="text-body1">
                      <q-icon name="copyright" />
                      copy rights <span>({{ copyrightYear }})</span>
                    </div>
              </div>
              <div class="footer__social_icons q-gutter-md">
                  <q-icon size="25px" name="mdi-facebook" tag="a" href="#" />
                  <q-icon size="25px" name="mdi-facebook-messenger"  tag="a" href="#" />
                  <q-icon size="25px" name="mdi-twitter" tag="a" href="#" />
                  <q-icon size="25px" name="mdi-google" tag="a" href="#" />
                  <q-icon size="25px" name="mdi-linkedin" tag="a" href="#" />
                  <q-icon size="25px" name="mdi-instagram" tag="a" href="#" />
              </div>
          </div>
      </div>
  </div>
</template>

<script setup>
import { date } from 'quasar'

const timeStamp = Date.now()
const copyrightYear = date.formatDate(timeStamp, 'YYYY')
</script>

<style lang="sass">
.footer__social_icons
    a
        text-decoration: none
        color: white
        cursor: pointer
        transition: transform 200ms ease-out
        &:hover
            transform: scale(1.5)
</style>