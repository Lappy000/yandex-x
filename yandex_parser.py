"""
Yandex Music parser module.
Extracts track information from Yandex Music pages.
"""

import requests
from bs4 import BeautifulSoup
import re
from typing import Dict, Optional


class YandexMusicParser:
    """Parser for extracting track information from Yandex Music."""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def validate_url(self, url: str) -> bool:
        """
        Validate if the URL is a valid Yandex Music track link.
        
        Args:
            url: The URL to validate
            
        Returns:
            True if valid, False otherwise
        """
        pattern = r'https?://music\.yandex\.(ru|com)/album/\d+/track/\d+'
        return bool(re.match(pattern, url))
    
    def parse_track(self, url: str) -> Optional[Dict[str, str]]:
        """
        Parse track information from Yandex Music URL.
        
        Args:
            url: Yandex Music track URL
            
        Returns:
            Dictionary with track info or None if parsing failed
        """
        if not self.validate_url(url):
            return None
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Extract track title
            title_elem = soup.find('h1', {'class': re.compile(r'.*title.*', re.I)})
            if not title_elem:
                title_elem = soup.find('meta', {'property': 'og:title'})
                title = title_elem.get('content', 'Unknown') if title_elem else 'Unknown'
            else:
                title = title_elem.get_text(strip=True)
            
            # Extract artist name
            artist_elem = soup.find('a', {'class': re.compile(r'.*artist.*', re.I)})
            if not artist_elem:
                artist_elem = soup.find('span', {'class': re.compile(r'.*artist.*', re.I)})
            if not artist_elem:
                # Try to extract from og:description or title
                desc_elem = soup.find('meta', {'property': 'og:description'})
                if desc_elem:
                    content = desc_elem.get('content', '')
                    if '—' in content:
                        artist = content.split('—')[0].strip()
                    else:
                        artist = 'Unknown'
                else:
                    artist = 'Unknown'
            else:
                artist = artist_elem.get_text(strip=True)
            
            # Extract duration
            duration_elem = soup.find('span', {'class': re.compile(r'.*duration.*', re.I)})
            if not duration_elem:
                duration_elem = soup.find('time')
            if not duration_elem:
                # Try to find duration in meta tags or scripts
                duration = 'Unknown'
                scripts = soup.find_all('script')
                for script in scripts:
                    if script.string and 'durationMs' in script.string:
                        match = re.search(r'"durationMs":(\d+)', script.string)
                        if match:
                            ms = int(match.group(1))
                            duration = self._format_duration(ms // 1000)
                            break
            else:
                duration = duration_elem.get_text(strip=True)
            
            return {
                'title': title,
                'artist': artist,
                'duration': duration,
                'url': url
            }
            
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"Parsing error: {e}")
            return None
    
    def _format_duration(self, seconds: int) -> str:
        """
        Format duration from seconds to MM:SS format.
        
        Args:
            seconds: Duration in seconds
            
        Returns:
            Formatted duration string
        """
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"