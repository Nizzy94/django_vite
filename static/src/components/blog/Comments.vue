<template>
    <div>
        <h6>Comments:</h6>
    </div>
    <q-list>
        <!-- <q-item > -->
        <comment :comment="comment" v-for="comment in comments" />
        <!-- </q-item> -->
    </q-list>
</template>

<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import Comment from "./Comment.vue";
const props = defineProps({
    comments: Array,
});
// const comments = ref([
//     {
//         id: 1,
//         parent: null,
//         children: [
//             {
//                 id: 2,
//                 parent: 1,
//                 children: [
//                     {
//                         id: 3,
//                         parent: 2,
//                         children: [],
//                         body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//                     },
//                 ],
//                 body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//             },
//         ],
//         body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//     },
//     {
//         id: 4,
//         parent: null,
//         children: [
//             {
//                 id: 5,
//                 parent: 4,
//                 children: [],
//                 body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//             },
//             {
//                 id: 6,
//                 parent: 4,
//                 children: [
//                     {
//                         id: 7,
//                         parent: 6,
//                         children: [],
//                         body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//                     },
//                 ],
//                 body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//             },
//         ],
//         body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//     },
//     {
//         id: 8,
//         parent: null,
//         children: [],
//         body: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
//     },
// ]);
</script>

<style>
</style>