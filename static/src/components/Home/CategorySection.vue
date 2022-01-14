<template>
   <div class="row q-gutter-xl q-px-xl">
            <div class="col" v-for="cat in (i, categories)" :key="cat.id">
              <div class="" style="height:300px">
                <q-card  class="category-card full-height column justify-evenly shadow-5" tag="a" href="#">
                    <q-card-section class="row justify-center">
                        <q-icon :name="cat.icon" size="50px" color="primary" />
                    </q-card-section>

                    <q-separator inset spaced />

                    <q-card-section>
                        <div class="text-h4 text-center">{{ cat.name }}</div>
                    </q-card-section>
                </q-card>
              </div>
            </div>
          </div>
</template>

<script setup>
    const categories = [
        {
            id:1,
            name: 'General',
            icon: 'mdi-newspaper-variant-outline'
        },
        {
            id:2,
            name: 'Sports',
            icon: 'mdi-tennis-ball'
        },
        {
            id:3,
            name: 'Politics',
            icon: 'mdi-account-tie'
        },
        {
            id:4,
            name: 'Entertainment',
            icon: 'mdi-music'
        },
        
    ]


</script>

<style lang="sass">
a.category-card
    text-decoration: none
    color: $dark
    transition: transform 200ms ease

    &:hover
        transform: scale(1.1)
</style>