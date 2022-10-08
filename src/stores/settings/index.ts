import { contextChildrenShowMode } from "@/composables/enums";
import { xxl } from "@/composables/useBreakpoints";
import { defineStore } from "pinia";

export default defineStore("settings", {
  state: () => ({
    use_np_img: false,
    use_sidebar: true,
    extend_width: false,
    contextChildrenShowMode: contextChildrenShowMode.click,
  }),
  actions: {
    toggleUseNPImg() {
      this.use_np_img = !this.use_np_img;
    },
    toggleDisableSidebar() {
      this.use_sidebar = !this.use_sidebar;
    },
    toggleExtendWidth() {
      this.extend_width = !this.extend_width;
    },
    setContextChildrenShowMode(mode: contextChildrenShowMode) {
      this.contextChildrenShowMode = mode;
    },
  },
  getters: {
    can_extend_width(): boolean {
      return xxl.value;
    },
  },
  persist: true,
});
