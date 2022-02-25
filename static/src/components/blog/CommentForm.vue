<template>
    <div class="q-my-md" v-if="user_is_authenticated">
        <q-input
            counter
            :maxlength="is_parent ? 500 : 300"
            :autofocus="!is_parent"
            autogrow
            type="textarea"
            :dense="!is_parent"
            v-model="comment"
            :label="is_parent ? 'Add Comment' : 'Add Reply'"
            @keyup.enter="submitComment"
            clearable
        />
        <q-btn
            :label="is_parent ? 'Add Comment' : 'Reply'"
            @click="submitComment"
            color="secondary"
            text-color="dark"
            class="q-mt-sm"
            :size="!is_parent ? '10px' : '14px'"
            :loading="sendingComment"
        />
    </div>
    <div v-else>
        <p>You must have an account to give comments.</p>
        <q-btn
            label="Login/Register"
            type="a"
            :href="`/login/auth/?next=${redirect_url}`"
            color="secondary"
            text-color="dark"
            class="q-mt-sm"
        />
    </div>
    <!-- </div> -->
</template>

<script setup>
import { ref, toRefs } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import postComment from "../../composables/postComment";

const props = defineProps({
    is_parent: {
        default: true,
        type: Boolean,
    },
    blog: {
        required: true,
        type: Number,
    },
    parent: {
        type: Number,
        default: null,
    },
});

const emit = defineEmits(["addComment"]);

const sendingComment = ref(false);

const redirect_url = window.location.pathname;

const user_is_authenticated = inject("user_is_authenticated");

const comment = ref("");

const { is_parent, blog, parent } = toRefs(props);

const { saveComment } = postComment();

const submitComment = async () => {
    sendingComment.value = true;
    const formData = {
        blog: blog.value,
        parent: parent.value,
        body: comment.value,
    };
    const res = await saveComment(formData);
    console.log(res);

    emit("addComment", res);

    comment.value = "";
    sendingComment.value = false;

    // console.log(formData);
};
</script>

<style>
</style>