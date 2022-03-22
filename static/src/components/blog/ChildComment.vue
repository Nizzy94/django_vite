
<script setup>
import { computed, ref, toRefs } from "@vue/reactivity";
import deleteCommentDialog from "../DeleteCommentDialog.vue";
import deleteComment from "../../composables/deleteComment";
import { inject } from "@vue/runtime-core";
import CommentForm from "./CommentForm.vue";

// name: "comment";

const props = defineProps({
    childComment: Object /** @type {Comment} */,
    authUser: Object,
    post_id: Number,
    parent: Number,
});

const emit = defineEmits(["deleteChildComm"]);

const { childComment, authUser, post_id, parent } = toRefs(props);

const user_is_authenticated = inject("user_is_authenticated");

const { removeComment } = deleteComment();

const showEditform = ref(false);

const delComDialog = ref(null);

const showConfirmDialog = () => {
    // console.log(delComDialog.value.confirmDialog);
    delComDialog.value.confirmDialog = true;
};

const updateComment = async (res) => {
    // console.log(res);
    showEditform.value = false;
    childComment.value.body = res.body;
    childComment.value.updated_at = res.updated_at;
    childComment.value.edited = res.edited;

    // comment.value
};

const delComment = async (data) => {
    // console.log("in delComment:before");
    const res = await removeComment(data);
    // console.log("in delComment:after");
    if (res.status == 200) {
        emit("deleteChildComm", { res: res, id: data.id });
    }
};
</script>

<template>
    <delete-comment-dialog
        ref="delComDialog"
        @delCom="delComment({ id: childComment?.id })"
    />
    <q-item>
        <q-card flat class="full-width childComment_card">
            <q-card-section :horizontal="!showEditform" class="justify-between">
                <transition
                    name="slide_form"
                    enter-active-class="animate__animated animate__fadeIn"
                    leave-active-class="animate__animated animate__fadeOut"
                    :duration="200"
                    mode="out-in"
                >
                    <q-card-section class="q-pt-none" v-if="showEditform">
                        <comment-form
                            :blog="post_id"
                            :parent="parent"
                            :value="childComment?.body"
                            @addComment="updateComment"
                            :is_parent="false"
                            @blurForm="showEditform = false"
                            :isEditForm="true"
                            :comment_id="childComment?.id"
                        />
                    </q-card-section>
                    <q-card-section v-else class="">
                        <q-field dense borderless hide-bottom-space>
                            <template v-slot:control>
                                <small class="full-width no-outline">
                                    {{ childComment?.body }}
                                </small>
                            </template>
                        </q-field>
                        <!-- {{ childComment?.body }} -->
                    </q-card-section>
                </transition>
                <q-card-section class="text-grey-7 self-center">
                    <small>
                        <strong>{{ childComment?.user.username }}</strong>
                        &bull;
                        {{ childComment?.created_at }}
                        <span v-if="childComment?.edited">
                            &bull; <strong> Edited:</strong>
                            {{ childComment?.updated_at }}
                        </span>
                    </small>
                </q-card-section>
            </q-card-section>
            <q-card-actions v-if="user_is_authenticated">
                <div class="row">
                    <div
                        v-if="
                            authUser?.username == childComment?.user?.username
                        "
                    >
                        <q-btn
                            :label="'Edit'"
                            flat
                            icon="mdi-square-edit-outline"
                            size="xs"
                            @click="showEditform = !showEditform"
                            color="grey-6"
                        />
                        <q-btn
                            :label="'Delete'"
                            flat
                            icon="mdi-delete"
                            size="xs"
                            @click="showConfirmDialog"
                            color="grey-6"
                        />
                    </div>
                </div>
            </q-card-actions>
        </q-card>
    </q-item>
</template>


<style lang="sass">
.childComment_card
    .q-card__section
        padding-top: 0
        padding-bottom: 0
</style>