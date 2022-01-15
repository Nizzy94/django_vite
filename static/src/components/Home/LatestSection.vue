<template>
<div class="column">

    <div class="row justify-center q-mb-lg">
        <div class="text-h2 text-center">Latest</div>
    </div>
    <div class="row q-col-gutter-md q-px-xl">
        <div class="col-xs-12 col-sm-6 col-md-3" v-for="(news,i) in latest" :key="news.id">
            <!-- <div class="" style="height:300px"> -->
               
                <news-card  
                :title="news.title" 
                :body="news.body" 
                subtitle="By John Doe" />
            <!-- </div> -->
        </div>
</div>
    </div>
</template>

<script setup>
import NewsCard from "../NewsCard.vue"

const latest = [
        {
            id:1,
            title: 'General Title',
            body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua consectetur adipiscing elit,.'
        },
        {
            id:2,
            title: 'Sports Title',
            body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        {
            id:3,
            title: 'Politics Title',
            body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        {
            id:4,
            title: 'Entertainment Titlesd',
            body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        
    ]
</script>

<style>

</style>