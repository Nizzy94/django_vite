
<script setup>
import { computed, reactive, ref, toRefs } from "@vue/reactivity";
import { inject, onBeforeMount, onMounted, watch } from "@vue/runtime-core";
import ChildComment from "./ChildComment.vue";
// import getAuthUser from "../../composables/getAuthUser";
import CommentForm from "./CommentForm.vue";
import deleteComment from "../../composables/deleteComment";
import deleteCommentDialog from "../DeleteCommentDialog.vue";

const props = defineProps({
    comment: Object,
    post_id: Number,
    authUser: Object,
});

const emit = defineEmits(["deleteComm"]);

const { comment, post_id, authUser } = toRefs(props);

// const authUser = ref({});

// const { callAuthUser } = getAuthUser();
const { removeComment } = deleteComment();

// onBeforeMount(async () => {
//     authUser.value = await callAuthUser();
// });

const user_is_authenticated = inject("user_is_authenticated");

// const comment_value = ref(comment.value.body);
const showReplyForm = ref(false);

const showEditform = ref(false);

const updateComment = async (res) => {
    // console.log(res);
    showEditform.value = false;
    comment.value.body = res.body;
    comment.value.updated_at = res.updated_at;
    comment.value.edited = res.edited;

    // comment.value
};

const addComment = async (res) => {
    showReplyForm.value = false;
    comment.value.children.unshift(res);
};

const delComDialog = ref(null);

// onMounted(() => console.log(delComDialog.value));

const showConfirmDialog = () => {
    // console.log(delComDialog.value.confirmDialog);
    delComDialog.value.confirmDialog = true;
};

const delComment = async (data) => {
    const res = await removeComment(data);
    if (res.status == 200) {
        emit("deleteComm", data.id);
    }
};
const delChildComment = async ({ res, id }) => {
    // const res = await removeComment(data);
    // console.log("in delChildComment:", res, id);
    if (res.status !== 200) return;
    emit("deleteComm", id);
};
</script>

<template>
    <delete-comment-dialog
        ref="delComDialog"
        @delCom="delComment({ id: comment?.id })"
    />
    <q-item>
        <q-card flat class="comment-card full-width q-mb-lg" square>
            <q-card-section>
                <div class="text-caption text-grey-7">
                    <strong>{{ comment?.user?.username }}</strong> &bull;
                    {{ comment?.created_at }}
                    <span v-if="comment?.edited">
                        &bull; <strong> Edited:</strong>
                        {{ comment?.updated_at }}
                    </span>
                </div>
            </q-card-section>

            <!-- leave-active-class="animate__animated animate__fadeInUp" -->

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
                        :value="comment?.body"
                        @addComment="updateComment"
                        @blurForm="showEditform = false"
                        :isEditForm="true"
                        :comment_id="comment?.id"
                    />
                </q-card-section>
                <q-card-section class="q-pt-none comment_body" v-else>
                    {{ comment?.body }}
                </q-card-section>
            </transition>

            <q-card-actions v-if="user_is_authenticated">
                <div class="row">
                    <div>
                        <q-btn
                            :label="!showReplyForm ? 'Reply' : 'close'"
                            flat
                            size="sm"
                            @click="showReplyForm = !showReplyForm"
                            color="primary"
                        />
                    </div>
                    <div v-if="authUser?.username == comment?.user?.username">
                        <q-btn
                            :label="'Edit'"
                            flat
                            icon="mdi-square-edit-outline"
                            size="sm"
                            @click="showEditform = !showEditform"
                            color="grey-6"
                        />
                        <q-btn
                            :label="'Delete'"
                            flat
                            icon="mdi-delete"
                            size="sm"
                            @click="showConfirmDialog"
                            color="grey-6"
                        />
                    </div>
                </div>
            </q-card-actions>
            <q-card-section v-if="showReplyForm">
                <comment-form
                    :blog="post_id"
                    :is_parent="false"
                    :parent="comment?.id"
                    @addComment="addComment"
                    @blurForm="showReplyForm = false"
                />
            </q-card-section>
            <q-card-section v-if="comment?.children?.length > 0">
                <q-list separator bordered class="comment-child-list q-pl-lg">
                    <!-- <q-item v-for="comment in comments"> -->
                    <child-comment
                        @deleteChildComm="delChildComment"
                        :childComment="child"
                        :authUser="authUser"
                        :post_id="post_id"
                        :parent="comment?.id"
                        v-for="child in comment?.children"
                    />
                    <!-- </q-item> -->
                </q-list>
            </q-card-section>
        </q-card>
    </q-item>
</template>


<style lang="sass">
.comment-card
    border-left: 3px solid $grey-4

    .comment-child-list
        border-left: none
        border-right: none
        font-size: 12px
</style>