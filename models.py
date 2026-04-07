from datetime import datetime


def create_models(db):
    """Factory function to create models with db instance"""
    
    class Article(db.Model):
        """Portfolio article model"""
        __tablename__ = 'articles'
        
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), nullable=False)
        description = db.Column(db.Text, nullable=False)
        image = db.Column(db.String(255), nullable=True)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        
        def __repr__(self):
            return f'<Article {self.title}>'


    class Service(db.Model):
        """Service/Solution model"""
        __tablename__ = 'services'
        
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text, nullable=False)
        icon = db.Column(db.String(50), default='star')
        
        def __repr__(self):
            return f'<Service {self.name}>'


    class AboutUs(db.Model):
        """Company About Us information"""
        __tablename__ = 'about_us'
        
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(200), default='About Admitionwala IT Services')
        company_description = db.Column(db.Text, nullable=False)
        vision = db.Column(db.Text, nullable=False)
        mission = db.Column(db.Text, nullable=False)
        about_founder = db.Column(db.Text, nullable=False)
        countries_served = db.Column(db.String(100), default='India, UK, USA')
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        
        def __repr__(self):
            return f'<AboutUs {self.title}>'


    class TeamMember(db.Model):
        """Team member model"""
        __tablename__ = 'team_members'
        
        # Role choices
        ROLES = {
            'founder': 'Founder & CEO',
            'technical_lead': 'Technical Lead',
            'marketing_head': 'Marketing Head',
            'developer': 'Developer',
            'designer': 'Designer',
            'manager': 'Project Manager',
            'other': 'Other'
        }
        
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(200), nullable=False)
        role = db.Column(db.String(50), nullable=False)
        description = db.Column(db.Text, nullable=False)
        image = db.Column(db.String(255), nullable=True)
        email = db.Column(db.String(120), nullable=True)
        phone = db.Column(db.String(20), nullable=True)
        linkedin_url = db.Column(db.String(255), nullable=True)
        twitter_url = db.Column(db.String(255), nullable=True)
        order = db.Column(db.Integer, default=0)
        is_active = db.Column(db.Boolean, default=True)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        
        def __repr__(self):
            return f'<TeamMember {self.name}>'
        
        def get_role_display(self):
            """Get human-readable role name"""
            return self.ROLES.get(self.role, self.role)

    return Article, Service, AboutUs, TeamMember
