<template>
  <div class="row q-mx-auto q-px-md" :class="{'q-px-xl':$q.screen.gt.sm}">
      <div class="author_image col-sm-5 col-xs-12">
          <q-card class="author_image__card q-mb-lg shadow-16" :class="{'full-width': $q.screen.lt.md}">
                <q-img src="https://cdn.quasar.dev/img/parallax2.jpg" />
            </q-card>
      </div>
      <div class="author_bio  col-sm-8 col-xs-12 relative-position offset-sm-4">
          <q-card class="author_bio__card  shadow-16" dark :class="{'full-width': $q.screen.lt.sm, 'floating_bio': $q.screen.gt.xs,
             'floating_bio_padding': $q.screen.sm, 'floating_bio_padding_big': $q.screen.gt.sm
          }">
            <q-card-section>
                <div class="text-h5 text-primary">Who is John Doe</div>
            </q-card-section>
            <q-card-section class="text-body2" >
                <p >
                    Aliquip amet eu culpa occaecat magna ut. Elit qui amet
                    occaecat reprehenderit cupidatat nisi qui do eu sunt. 
                    Labore anim dolore non anim dolore mollit consequat do commodo
                    esse esse eu Lorem aliquip. Cupidatat minim est id dolor veniam 
                    nulla laboris anim sit culpa esse. Nulla velit incididunt ad non 
                    adipisicing enim. Velit nulla id esse ad fugiat labore labore.
                </p>
                <p >
                    Aliquip amet eu culpa occaecat magna ut. Elit qui amet
                    occaecat reprehenderit cupidatat nisi qui do eu sunt. 
                    Labore anim dolore non anim dolore mollit consequat do commodo
                    esse esse eu Lorem aliquip. Cupidatat minim est id dolor veniam 
                    nulla laboris anim sit culpa esse. Nulla velit incididunt ad non 
                    adipisicing enim. Velit nulla id esse ad fugiat labore labore.
                </p>
                <p >
                    Aliquip amet eu culpa occaecat magna ut. Elit qui amet
                    occaecat reprehenderit cupidatat nisi qui do eu sunt. 
                    Labore anim dolore non anim dolore mollit consequat do commodo
                    esse esse eu Lorem aliquip. Cupidatat minim est id dolor veniam 
                    nulla laboris anim sit culpa esse. Nulla velit incididunt ad non 
                    adipisicing enim. Velit nulla id esse ad fugiat labore labore.
                </p>
            </q-card-section>

        </q-card>
      </div>
  </div>
</template>

<script setup>
</script>

<style lang="sass">
// .author_image__card
//     width: 300px
    // height: 300px

.floating_bio
    position: absolute
    top: -300px
    right: 0
    z-index: -1
    // padding-left: 130px

.floating_bio_padding_big
    padding-left: 130px
.floating_bio_padding
    padding-left: 80px


</style>