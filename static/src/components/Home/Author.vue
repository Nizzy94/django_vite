<template>
    <div class="">
        <!-- <div class="col-xs-12 col-md-6">
          <q-img height="400px" src="https://cdn.quasar.dev/img/parallax1.jpg" alt="author image" />
      </div>
      <div class="col-xs-12 col-md-6"></div> -->
        <!-- <div class="text-center q-mb-xl">
          <div class="text-h2 text-white">Author</div>
      </div> -->
        <q-card
            class="my-card bg-teal-9 shadow-0"
            dark
            square
            v-if="$q.screen.gt.sm"
        >
            <q-card-section horizontal class="row q-py-lg">
                <q-card-section class="col-5 flex justify-center">
                    <!-- <div
                        data-aos="fade-right"
                        data-aos-duration="1000"
                        data-aos-delay="1500"
                    > -->
                    <q-avatar
                        size="300px"
                        class=""
                        data-aos="fade-right"
                        data-aos-duration="1000"
                        data-aos-delay="1500"
                    >
                        <img src="https://cdn.quasar.dev/img/avatar.png" />
                    </q-avatar>
                    <!-- </div> -->
                </q-card-section>

                <q-separator vertical dark />

                <q-card-section>
                    <!-- <div
                        data-aos-duration="1500"
                        data-aos="fade-left"
                        data-aos-delay="1500"
                    > -->
                    <div
                        class=""
                        data-aos-duration="1500"
                        data-aos="fade-up"
                        data-aos-delay="1500"
                    >
                        <div class="text-h3 text-center q-mb-xl text-white">
                            Hi, I'm John Doe
                        </div>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit, sed do eiusmod tempor incididunt ut labore et
                            dolore magna aliqua consectetur adipiscing elit.
                        </p>
                    </div>
                    <!-- </div> -->
                    <q-card-actions align="center">
                        <q-btn
                            flat
                            color="white"
                            class=""
                            type="a"
                            :href="`${routes.about}#author__about`"
                        >
                            Read More
                        </q-btn>
                    </q-card-actions>
                </q-card-section>
            </q-card-section>

            <!-- <q-separator dark /> -->
        </q-card>
        <q-card class="my-card bg-teal-9 shadow-0" dark square v-else>
            <q-card-section horizontal class="column q-py-lg">
                <q-card-section class="flex justify-center">
                    <q-avatar
                        size="200px"
                        class=""
                        data-aos-duration="1000"
                        data-aos="fade-right"
                    >
                        <img src="https://cdn.quasar.dev/img/avatar.png" />
                    </q-avatar>
                </q-card-section>

                <q-separator dark />

                <q-card-section>
                    <div data-aos-duration="1500" data-aos="fade-left">
                        <div class="text-center q-mb-xl">
                            <div class="text-h3 text-white">Author</div>
                        </div>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit, sed do eiusmod tempor incididunt ut labore et
                            dolore magna aliqua consectetur adipiscing elit.
                        </p>
                    </div>
                </q-card-section>
            </q-card-section>

            <q-separator dark />

            <q-card-actions align="center">
                <q-btn
                    flat
                    color="white"
                    class=""
                    type="a"
                    :href="`${routes.about}#author__about`"
                >
                    Read More
                </q-btn>
            </q-card-actions>
        </q-card>
    </div>
</template>

<script setup>
import { inject } from "@vue/runtime-core";

console.log(inject("routes").value);

const routes = inject("routes");
</script>

<style>
</style>