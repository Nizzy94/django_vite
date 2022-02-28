<template>
    <div>
        <h6>Comments:</h6>
    </div>
    <div class="q-ma-md">
        <comment-form :blog="post_id" @addComment="addComment" />
    </div>
    <q-toggle v-model="showComments" label="View Comments" class="q-mb-md" />

    <q-slide-transition>
        <div v-show="showComments">
            <q-list separator>
                <!-- <q-item > -->
                <comment
                    :comment="comment"
                    :post_id="post_id"
                    v-for="comment in comments"
                />
                <!-- </q-item> -->
            </q-list>
        </div>
    </q-slide-transition>
</template>

<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import Comment from "./Comment.vue";
import CommentForm from "./CommentForm.vue";
import moment from "moment";

const props = defineProps({
    comments: Array,
    post_id: Number,
});
// const commentForm = ref(null);

const { comments, post_id } = toRefs(props);

const showComments = ref(true);

const addComment = async (res) => {
    console.log(res);
    comments.value.unshift(res);
    showComments.value = true;
};
</script>

<style>
</style>