from playwright.sync_api import sync_playwright

class BuzzPage:
    def __init__(self,page):
        self.page = page
        self.share_photos = page.get_by_role("button", name="Share Photos")
        self.share_videos = page.get_by_role("button", name="Share Video")
        self.share_thoughts = page.locator("//div[@class='orangehrm-buzz-post-modal-header-text']//textarea[@placeholder='What's on your mind?']")
        self.text_post = page.locator("textarea.oxd-buzz-post-input")
        self.photos = page.locator("input[type='file']")
        self.video_url = page.get_by_role("textbox", name="Paste Video URL")
        self.share = page.get_by_text("Share", exact=True)
        self.post = page.get_by_text("Post", exact=True) 

    def post_text(self, text_post):
        self.text_post.fill(text_post)
        self.post.click()


    def post_image(self, path):
        self.share_photos.click()
        self.photos.set_input_files(path)
        self.share.click()

    def post_video(self, text_post, v_path):
        self.share_videos.click()
        self.video_url.click()
        self.video_url.fill(v_path)
        self.share.click()

        


        


        
    
