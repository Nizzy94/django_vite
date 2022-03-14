<template>
    <q-dialog v-model="confirmDialog" persistent>
        <q-card>
            <q-card-section
                class="row items-center bg-primary text-white text-bold"
            >
                <q-avatar icon="warning" color="negative" text-color="white" />
                <span class="q-ml-sm text-body1"> Confirm Delete! </span>
            </q-card-section>
            <q-card-section class="row items-center">
                <!-- <q-avatar icon="warning" color="primary" text-color="white" /> -->
                <span class="q-ml-sm">
                    Are you sure you want to delete this comment?
                </span>
            </q-card-section>

            <q-card-actions align="right">
                <q-btn flat label="Cancel" color="primary" v-close-popup />
                <q-btn
                    flat
                    label="Delete"
                    color="negative"
                    @click="deleteComm"
                />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { ref } from "@vue/reactivity";

const confirmDialog = ref(false);
const successDialog = ref(false);
const emit = defineEmits(["delCom"]);
const deleteComm = async () => {
    emit("delCom");
    confirmDialog.value = false;
    // successDialog.value = true;
};

defineExpose({ confirmDialog });
</script>

<style>
</style>