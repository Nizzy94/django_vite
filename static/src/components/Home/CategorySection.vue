<template>
   <div  class="row q-col-gutter-lg q-px-xl justify-center">
       <!-- <q-intersection > -->
        <q-intersection transition="slide-up" once 
            :transition-duration="500+(200*i)" 
            class="col-xs-12 col-sm-6 col-md-3" 
            v-for="(cat,i) in categories" :key="cat.id">
           
            <div  class="" style="height:200px">
                <q-card  class="category-card full-height column justify-evenly shadow-10" tag="a" href="#">
                    <q-card-section class="row justify-center">
                        <q-icon :name="cat.icon" size="50px" color="primary" />
                    </q-card-section>

                    <q-separator inset spaced />

                    <q-card-section>
                        <div class="text-h4 text-center">{{ cat.name }}</div>
                    </q-card-section>
                </q-card>
            </div>
        </q-intersection>
       <!-- </q-intersection> -->
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
        {
            id:4,
            name: 'Health',
            icon: 'mdi-stethoscope'
        },
        
    ]


</script>

<style lang="sass">
a.category-card
    text-decoration: none
    color: $dark
    transition: transform 500ms ease

    &:hover
        transform: scale(1.05)
</style>