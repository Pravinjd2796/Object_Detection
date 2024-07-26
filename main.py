
# import os
# import streamlit as st
# from detect_objects import detect_objects
# from results_storage import save_results, load_results
# from generate_copy import generate_copywriting

# def main():
#     st.title('Object Detection and Copywriting Service')

#     uploaded_file = st.file_uploader("Upload a video", type=["mp4"])
#     if uploaded_file:
#         st.write("File uploaded successfully.")
#         video_path = os.path.join('temp', uploaded_file.name)
#         st.write(f"Saving file to {video_path}")
#         os.makedirs('temp', exist_ok=True)
#         with open(video_path, "wb") as f:
#             f.write(uploaded_file.getvalue())

#         # Perform detection and save results
#         st.write("Running object detection...")
#         results = detect_objects(video_path)
#         st.write("Saving results...")
#         save_results(results, 'results')

#         st.write("Object Detection Results:")
#         st.json(results)

#         # Generate copywriting
#         st.write("Generating copywriting...")
#         copywriting = generate_copywriting(results)
#         st.write("Generated Copywriting:")
#         st.text(copywriting)

import os
import streamlit as st
from detect_objects import detect_objects
from results_storage import save_results, load_results
from generate_copy import generate_copywriting

# def main():
#     st.title('Object Detection and Copywriting Service')

#     uploaded_file = st.file_uploader("Upload a video", type=["mp4"])
#     if uploaded_file:
#         st.write("File uploaded successfully.")
        
#         # Save uploaded file
#         video_path = os.path.join('temp', uploaded_file.name)
#         st.write(f"Saving file to {video_path}")
#         os.makedirs('temp', exist_ok=True)
#         with open(video_path, "wb") as f:
#             f.write(uploaded_file.getvalue())

#         # Perform detection and save results
#         st.write("Running object detection...")
#         try:
#             results = detect_objects(video_path)
#             st.write("Detection results:", results)
#         except Exception as e:
#             st.error(f"Error during object detection: {e}")
#             return
        
#         st.write("Saving results...")
#         try:
#             save_results(results, 'results')
#         except Exception as e:
#             st.error(f"Error saving results: {e}")
#             return

#         st.write("Object Detection Results:")
#         st.json(results)

#         # Generate copywriting
#         st.write("Generating copywriting...")
#         try:
#             copywriting = generate_copywriting(results)
#             st.write("Generated Copywriting:")
#             st.text(copywriting)
#         except Exception as e:
#             st.error(f"Error generating copywriting: {e}")

# if __name__ == "__main__":
#     main()
def main():
    st.title('Object Detection and Copywriting Service')

    uploaded_file = st.file_uploader("Upload a video", type=["mp4"])
    if uploaded_file:
        st.write("File uploaded successfully.")
        
        video_path = os.path.join('temp', uploaded_file.name)
        st.write(f"Saving file to {video_path}")
        os.makedirs('temp', exist_ok=True)
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Perform detection and save results
        st.write("Running object detection...")
        try:
            results = detect_objects(video_path)
            st.write("Detection results:", results)
        except Exception as e:
            st.error(f"Error during object detection: {e}")
            return
        
        st.write("Saving results...")
        try:
            save_results(results, 'results')
        except Exception as e:
            st.error(f"Error saving results: {e}")
            return

        st.write("Object Detection Results:")
        st.json(results)

        # Generate copywriting
        st.write("Generating copywriting...")
        try:
            copywriting = generate_copywriting(results)
            st.write("Generated Copywriting:")
            st.text(copywriting)
        except Exception as e:
            st.error(f"Error generating copywriting: {e}")

if __name__ == "__main__":
    main()