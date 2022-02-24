<template>
    <div class="q-my-md" v-if="user_is_authenticated">
        <q-input
            :dense="!parent"
            v-model="comment"
            :label="parent ? 'Add Comment' : 'Add Reply'"
        />
        <q-btn
            :label="parent ? 'Add Comment' : 'Reply'"
            @click="submitComment"
            color="secondary"
            text-color="dark"
            class="q-mt-sm"
            :size="!parent ? '10px' : '14px'"
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

const props = defineProps({
    parent: {
        default: true,
        type: Boolean,
    },
    post_id: {
        required: true,
        type: Number,
    },
    parent_id: {
        type: Number,
        default: null,
    },
});

const redirect_url = window.location.pathname;

const user_is_authenticated = inject("user_is_authenticated");

const comment = ref("");

const { parent, post_id, parent_id } = toRefs(props);

const submitComment = () => {
    const formData = {
        parent: parent.value,
        post_id: post_id.value,
        parent_id: parent_id.value,
        comment: comment.value,
    };

    console.log(formData);
};
</script>

<style>
</style>