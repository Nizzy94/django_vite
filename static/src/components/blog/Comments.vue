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
                    @deleteComm="deleteComm"
                    :comment="comment"
                    :post_id="post_id"
                    v-for="comment in comments"
                    :authUser="authUser"
                />
                <!-- </q-item> -->
            </q-list>
        </div>
    </q-slide-transition>
</template>

<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import { inject, onBeforeMount } from "@vue/runtime-core";
import Comment from "./Comment.vue";
import CommentForm from "./CommentForm.vue";
import moment from "moment";
import getComments from "../../composables/getComments";
import getAuthUser from "../../composables/getAuthUser";
import { useQuasar } from "quasar";

const props = defineProps({
    // comments: Array,
    post_id: Number,
});

const { post_id } = toRefs(props);

const $q = useQuasar();

const { callComments, comments } = getComments();

const { callAuthUser } = getAuthUser();

const user_is_authenticated = inject("user_is_authenticated");
const authUser = ref({});

onBeforeMount(async () => {
    if (user_is_authenticated) {
        authUser.value = await callAuthUser();
    }
});

callComments(post_id.value);

const showComments = ref(true);

const addComment = async (res) => {
    console.log(res);
    comments.value.unshift(res);
    showComments.value = true;
};

// const dynamicCommentList = computed(() => {
//     return comments.value?.filter((comment) => comment.id != id);
// })

const deleteComm = async (id) => {
    await callComments(post_id.value);
    $q.notify({
        type: "positive",
        message: "Comment has been deleted.",
        position: "top-right",
    });
};
</script>

<style>
</style>