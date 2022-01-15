<template>
  <div class="">
      <!-- <div class="col-xs-12 col-md-6">
          <q-img height="400px" src="https://cdn.quasar.dev/img/parallax1.jpg" alt="author image" />
      </div>
      <div class="col-xs-12 col-md-6"></div> -->
      <!-- <div class="text-center q-mb-xl">
          <div class="text-h2 text-white">Author</div>
      </div> -->
      <q-card class="my-card  bg-dark " dark square >
        <q-card-section horizontal class="row q-py-lg">
            <q-card-section class="col-5 flex justify-center">
                <q-avatar size="300px">
                    <img src="https://cdn.quasar.dev/img/avatar.png">
                </q-avatar>
            </q-card-section>

            <q-separator vertical dark />


            <q-card-section>
                <div class="text-center q-mb-xl">
                    <div class="text-h3 text-white">Author</div>
                </div>
                <p>Lorem ipsum dolor sit amet, 
                    consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt
                    ut labore et dolore magna 
                    aliqua consectetur adipiscing elit.
                </p>
            </q-card-section>
        </q-card-section>

        <q-separator dark />

        <q-card-actions align="center">
            
            <q-btn flat color="white">
            Read More
            </q-btn>
        </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>