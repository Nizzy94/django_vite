<template>
    <div>
        <h6>Comments:</h6>
    </div>
    <div class="q-ma-md">
        <comment-form :blog="post_id" @addComment="addComment" />
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
// const commentForm = ref(null);

const { comments, post_id } = toRefs(props);

const addComment = async (res) => {
    console.log(res);
    comments.value.unshift(res);
};
</script>

<style>
</style>