<template>
    <div class="q-mb-md" v-if="user_is_authenticated">
        <!-- @blur="is_parent && !isEditForm ? '' : formBlured" -->
        <!-- @blur="
                is_parent && !isEditForm
                    ? ''
                    : submitComment({ withBlur: true })
            " -->
        <q-input
            counter
            :maxlength="is_parent ? 500 : 300"
            @blur="formBlured"
            :autofocus="!is_parent || isEditForm"
            :autogrow="is_parent"
            :type="is_parent ? 'textarea' : 'text'"
            :dense="!is_parent"
            v-model="comment"
            :error="commentFormError != ''"
            :error-message="commentFormError"
            :label="isEditForm ? '' : is_parent ? 'Add Comment' : 'Add Reply'"
            @keyup.enter="submitComment({ withEnter: true })"
            clearable
        />
        <q-btn
            :label="isEditForm ? 'Edit' : is_parent ? 'Add Comment' : 'Reply'"
            @click="submitComment({})"
            color="secondary"
            text-color="dark"
            class="q-mt-sm commentFormSubmitBtn"
            :size="isEditForm ? '10px' : !is_parent ? '10px' : '14px'"
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
import { inject, onMounted } from "@vue/runtime-core";
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
    value: {
        type: String,
        default: null,
    },
    isEditForm: {
        type: Boolean,
        default: false,
    },
    comment_id: {
        type: Number,
        default: null,
    },
});

const emit = defineEmits(["addComment", "blurForm"]);

const sendingComment = ref(false);

const redirect_url = window.location.pathname;

const user_is_authenticated = inject("user_is_authenticated");

const comment = ref("");

const { is_parent, blog, parent, value, isEditForm, comment_id } =
    toRefs(props);

const commentFormError = ref("");

if (value.value) comment.value = value.value;

const { saveComment } = postComment();

const submitComment = async ({ withEnter = false }) => {
    // console.log(withEnter);
    // console.log(is_parent.value);
    // console.log(isEditForm.value);
    if (withEnter && is_parent.value && !isEditForm.value) return;

    // console.log("not returned");
    sendingComment.value = true;
    const formData = {
        blog: blog.value,
        parent: parent.value,
        body: comment.value,
        id: comment_id.value,
        edited: isEditForm.value,
    };
    // console.log(formData);
    const res = await saveComment(formData);
    // console.log(res);

    if (res.status == 200) {
        emit("addComment", res.data);

        comment.value = "";
        commentFormError.value = "";
    } else {
        if (res.status == 400) {
            // console.log(res.data);
            commentFormError.value = res.data.body[0];
        }
    }

    sendingComment.value = false;

    // console.log(formData);
};

const formBlured = (e) => {
    if (is_parent.value && !isEditForm.value) return;

    if (e.relatedTarget?.classList.contains("commentFormSubmitBtn")) return;

    emit("blurForm");
};
</script>

<style>
</style>