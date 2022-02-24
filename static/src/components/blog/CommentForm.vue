<template>
    <q-input v-model="comment" :label="parent ? : 'Add Comment':'Add Reply'" />
    <q-btn :label="parent ? : 'Add Comment':'Reply'" @click="submitComment" />
</template>

<script setup>
import { toRefs } from "@vue/reactivity";

const props = defineProps({
    parent: {
        default: true,
        type: Boolean,
    },
    post_id: {
        required: true,
        type: Number,
    },
    parent_id: Number,
});

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