# 凱伊 AI 繪圖室 — 離線 Android 版

這是一份**可直接上傳 GitHub 的建置專案**，使用開源 [Local Dream](https://github.com/xororz/local-dream) 作為手機端 Stable Diffusion 推論引擎。它不是從零重寫的完整模型原始碼；GitHub Actions 會在編譯時自動下載上游完整程式碼與子模組。

## 最簡單的使用方式

1. 將本 ZIP 解壓縮，**把內部的 `.github` 和 `scripts` 資料夾、`README.md` 一起上傳至 GitHub 儲存庫根目錄**，覆蓋舊的 `.github/workflows/build-apk.yml`。注意 `.github` 是隱藏資料夾，解壓縮工具須顯示隱藏檔。
2. 開啟儲存庫 Actions → `Build Kei Offline Drawing APK` → `Run workflow`。
3. 執行成功後，在該次 Actions 頁面的 Artifacts 下載 `KeiOfflineStudio-Android-APK`，解壓縮並安裝 APK。
4. 在 App 中下載或匯入支援的模型，才可進行**真正的離線繪圖**。模型不包含在 APK 內；首次取得模型通常需要網路，之後依模型支援情況離線使用。

## 目前的功能與限制

- 保留 Local Dream 原本的手機端繪圖、模型管理與歷史紀錄功能；App 顯示名稱改為「凱伊 AI 繪圖室」。
- 使用 Android 預設 debug 簽署，不需要上傳任何 keystore。
- 這個版本**尚未**更換角色圖示、客製完整 UI 或加入 AI 聊天。
- 目前 APK 是**測試版**，不適合正式上架；未來發行應改用安全保存的固定簽署金鑰。
- 目前 workflow 使用上游預設分支，若上游修改 build.gradle.kts，prepare.py 會故意報錯以避免錯誤修改。
- 離線推論的速度與可用性取決於 Android 裝置 CPU/GPU/NPU、RAM 與模型格式；部分模型可能無法在你的手機上執行。
- 此 ZIP 不是現成 APK。必須在 GitHub Actions 成功編譯後才能下載安裝。
- 由於執行環境無法取得 Android SDK 或下載上游大型原始碼，**尚未實際執行 APK 編譯**。

上游程式碼版權與授權仍由原專案及其依賴授權規範。
