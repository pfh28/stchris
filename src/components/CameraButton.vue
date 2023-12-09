<template>
    <label for="cameraFileInput" class="w-8 h-8">
        <div class="bg-gray-400 w-full h-full rounded-lg grid place-content-center cursor-pointer">
            <div class="w-6 h-6"><CameraIcon/></div>
        </div>
        <input id="cameraFileInput"
                @change="handleImage" 
                type="file" 
                accept="image/*" 
                capture="environment"
                class="invisible" />
    </label>
</template>
<script setup>
import {CameraIcon} from '@heroicons/vue/24/outline'

const props = defineProps({modelValue: Object})

const emit = defineEmits(['fileAdded'])

function handleImage(event) {
    emit('fileAdded', event.target.files)
}
</script>