<template>
    <div>
        <h6>Comments:</h6>
    </div>
    <div class="q-ma-md">
        <comment-form :post_id="post_id" />
    </div>
    <q-list>
        <!-- <q-item > -->
        <comment
            :comment="comment"
            :post_id="post_id"
            v-for="comment in comments"
        />
        <!-- </q-item> -->
    </q-list>
</template>

<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import Comment from "./Comment.vue";
import CommentForm from "./CommentForm.vue";
const props = defineProps({
    comments: Array,
    post_id: Number,
});

const { comments, post_id } = toRefs(props);

// const post_id = inject("post_id");
</script>

<style>
</style>