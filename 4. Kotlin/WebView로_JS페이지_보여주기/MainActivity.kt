package com.example.practiceapp

import android.app.Dialog
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Message
import android.view.ViewGroup
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val webView : WebView = findViewById(R.id.testWebView);

        webView.apply {
            webViewClient = WebViewClient()

            webChromeClient = object : WebChromeClient() {
                override fun onCreateWindow(
                    view: WebView?,
                    isDialog: Boolean,
                    isUserGesture: Boolean,
                    resultMsg: Message?
                ): Boolean {
                    val newWebView = WebView(this@MainActivity).apply {
                        webViewClient = WebViewClient()
                        settings.javaScriptEnabled = true
                    }

                    val dialog = Dialog(this@MainActivity).apply {
                        setContentView(newWebView)
                        window!!.attributes.width = ViewGroup.LayoutParams.MATCH_PARENT
                        window!!.attributes.height = ViewGroup.LayoutParams.MATCH_PARENT
                        show()
                    }

                    newWebView.webChromeClient = object : WebChromeClient() {
                        override fun onCloseWindow(window: WebView?) {
                            dialog.dismiss()
                        }
                    }

                    (resultMsg?.obj as WebView.WebViewTransport).webView = newWebView
                    resultMsg.sendToTarget()

                    return true
                }
            }

            settings.javaScriptEnabled = true
            settings.setSupportMultipleWindows(true) // 새창띄우기 허용
            settings.javaScriptCanOpenWindowsAutomatically = true // 자바스크립트 새창 띄우기
            settings.loadWithOverviewMode = true // 메타태크 허용
            settings.useWideViewPort = true // 화면 사이즈 맞추기
            settings.setSupportZoom(true) // 화면 줌 허용
            settings.builtInZoomControls = true // 화면 확대/축소 허용

            settings.cacheMode =
                WebSettings.LOAD_NO_CACHE // 브라우저 캐시
            settings.domStorageEnabled = true // 로컬저장소 허용
            settings.displayZoomControls = true
        }
        webView.loadUrl("file:///android_asset/www/index.html");
    }
}